<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'
import type { BorrowedBook } from '@/types'

export default defineComponent({
  name: 'BorrowedBooksView',
  setup() {
    const borrowedBooks = ref<BorrowedBook[]>([])

    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1/students'

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
      formatDate
    }
  }
})
</script>

<style scoped>
/* Custom styles (if needed) */
</style>

<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="w-full max-w-4xl bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Borrowed Books</h2>
      <table class="min-w-full bg-white">
        <thead class="bg-gray-200">
          <tr>
            <th class="py-2 px-4 text-left">Title</th>
            <th class="py-2 px-4 text-left">Author</th>
            <th class="py-2 px-4 text-left">Borrowed Date</th>
            <th class="py-2 px-4 text-left">Return Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in borrowedBooks" :key="book.id">
            <td class="py-2 px-4">{{ book.book.title }}</td>
            <td class="py-2 px-4">{{ book.book.title }}</td>
            <td class="py-2 px-4">{{ formatDate(book.borrow_date) }}</td>
            <td class="py-2 px-4">{{ formatDate(book.return_date) }}</td>
          </tr>
        </tbody>
      </table>
      <button
        @click="goBack"
        class="mt-6 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
      >
        Go Back
      </button>
    </div>
  </div>
</template>
