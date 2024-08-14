<template>
  <div class="flex justify-center items-start min-h-screen bg-gray-100 p-4 sm:p-12">
    <div class="w-full max-w-4xl bg-white shadow-lg rounded-lg p-6  sm:p-8">
      <h2 class="text-2xl sm:text-3xl font-extrabold mb-6 text-center text-gray-800">
        Borrowed Books
      </h2>
      <div class="overflow-x-auto">
        <table class="min-w-full bg-white border border-gray-200">
          <thead class="bg-gray-700">
            <tr>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">Title</th>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">Author</th>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">Borrowed Date</th>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">Return Date</th>
              <th class="py-3 px-4 text-center text-white border-b border-gray-200">Actions</th>
            </tr>
          </thead>
          <tbody class="text-gray-600">
            <tr
              v-for="book in borrowedBookData?.borrowed_books"
              :key="book.id"
              class="border-t border-gray-200 hover:bg-gray-100"
            >
              <td class="py-3 px-4">{{ book.book.title }}</td>
              <td class="py-3 px-4">{{ book.book.author }}</td>
              <td class="py-3 px-4">{{ formatDate(book.borrow_date) }}</td>
              <td class="py-3 px-4">{{ formatDate(book.return_date) }}</td>
              <td class="py-3 px-4 text-center">
                <button
                  @click="returnBook(book.book.id)"
                  :disabled="returning[book.book.id]"
                  class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                  {{ returning[book.book.id] ? 'Returning...' : 'Return' }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <button
        @click="goBack"
        class="mt-6 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
      >
        Go Back
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/useUserStore'
import { computed } from 'vue'

export default defineComponent({
  name: 'BorrowedBooksView',
  setup() {
    // const borrowedBooks = ref<BorrowedBook | []>([])
    const returning = ref<{ [key: string]: boolean }>({})
    const userStore = useUserStore()

    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1'

    const borrowedBookData = computed(() => {
      return userStore.borrowedBooks
    })

    const returnBook = async (bookId: string) => {
      try {
        const token = localStorage.getItem('token')
        if (!token) throw new Error('Token not found')

        returning.value[bookId] = true

        await axios.post(
          `${BASE_URL}/books/return`,
          { borrowed_book_id: bookId },
          { headers: { Authorization: `Bearer ${token}` } }
        )

        return userStore.borrowedBook()
      } catch (error) {
        console.error('Error returning book:', error)
        alert('Failed to return book')
      } finally {
        returning.value[bookId] = false
      }
    }

    const formatDate = (dateString: string) => {
      const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(dateString).toLocaleDateString(undefined, options)
    }

    const goBack = () => {
      window.history.back()
    }

    onMounted(async () => {
      await userStore.borrowedBook()
    })

    return {
      goBack,
      formatDate,
      returnBook,
      returning,
      borrowedBookData
    }
  }
})
</script>
