<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'
import type { BorrowedBook } from '@/types'

export default defineComponent({
  name: 'BorrowedBooksView',
  setup() {
    const borrowedBooks = ref<BorrowedBook[]>([])
    const returning = ref<{ [key: string]: boolean }>({})

    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1'

    const fetchBorrowedBooks = async () => {
      try {
        const token = localStorage.getItem('token')
        if (!token) throw new Error('Token not found')

        const response = await axios.get(`${BASE_URL}/books/borrowed`, {
          headers: { Authorization: `Bearer ${token}` }
        })

        borrowedBooks.value = response.data.data.borrowed_books
      } catch (error) {
        console.error('Error fetching borrowed books:', error)
      }
    }

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

        fetchBorrowedBooks()
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

    onMounted(() => {
      fetchBorrowedBooks()
    })

    return {
      borrowedBooks,
      goBack,
      formatDate,
      returnBook,
      returning
    }
  }
})
</script>

<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100 p-4 sm:p-12">
    <div class="w-full max-w-4xl bg-white shadow-lg rounded-lg p-6 sm:p-8">
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
              v-for="book in borrowedBooks"
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
