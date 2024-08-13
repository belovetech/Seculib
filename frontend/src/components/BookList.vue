<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import axios, { AxiosError } from 'axios'
import { useUserStore } from '@/stores/useUserStore'
import type { Book } from '@/types'

export default defineComponent({
  name: 'BookList',
  setup() {
    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1'
    const books = ref<Book[]>([])
    const userStore = useUserStore()

    const fetchBooks = async () => {
      try {
        const response = await axios.get(`${BASE_URL}/books`)
        books.value = response.data.data
      } catch (e) {
        const error = e as AxiosError
        const message = error.response?.data as { message: string }
        alert(message.message)
        console.error(error)
      }
    }

    const borrowBook = async (id: string) => {
      if (!userStore.isAuthenticated) {
        alert('Please log in to borrow a book.')
        return
      }

      try {
        await axios.post(`${BASE_URL}/borrow`, {
          book_id: id
        })
        fetchBooks()
      } catch (error) {
        console.error('Error borrowing the book:', error)
        alert('Failed to borrow the book. Please try again later.')
      }
    }

    onMounted(fetchBooks)

    return {
      books,
      borrowBook
    }
  }
})
</script>

<style scoped>
/* Additional styles, if needed */
</style>

<template>
  <div class="py-10">
    <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-500">Available Books</h2>
    <ul class="space-y-4">
      <li
        v-for="book in books"
        :key="book.id"
        class="p-4 bg-white rounded-lg shadow-md flex justify-between items-center"
      >
        <div>
          <h3 class="text-xl font-semibold text-gray-900">{{ book.title }}</h3>
          <p class="text-gray-700">by {{ book.author }}</p>
        </div>
        <button
          v-if="book.available"
          @click="borrowBook(book.id)"
          class="bg-green-500 hover:bg-green-700 text-white py-2 px-4 rounded-lg focus:outline-none focus:shadow-outline"
        >
          Borrow
        </button>
      </li>
    </ul>
  </div>
</template>
