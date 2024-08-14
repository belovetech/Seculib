<template>
  <div class="py-6">
    <h2 class="text-2xl font-extrabold mb-2 text-center text-gray-500">
      {{ books.length }} Available Books
    </h2>
    <ul class="space-y-3">
      <li
        v-for="book in books"
        :key="book.id"
        class="p-4 bg-white rounded-lg shadow-md flex justify-between items-center"
      >
        <div>
          <h3 class="text-md font-semibold text-gray-900">{{ book.title }}</h3>
          <p class="text-gray-700">by {{ book.author }}</p>
        </div>
        <button
          v-if="book.available"
          @click="borrowBook(book.id)"
          :disabled="borrowing[book.id]"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-lg shadow-md focus:outline-none focus:shadow-outline"
        >
          {{ borrowing[book.id] ? 'Borrowing...' : 'Borrow' }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import axios, { AxiosError } from 'axios'
import type { Book } from '@/types'
import { useUserStore } from '@/stores/useUserStore'

export default defineComponent({
  name: 'BookList',
  setup() {
    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1'
    const books = ref<Book[]>([])
    const borrowing = ref<{ [key: string]: boolean }>({})
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
      const token = localStorage.getItem('token')
      if (!token) {
        alert('You need to login to borrow a book')
        return
      }

      borrowing.value[id] = true // Disable the button for this book

      try {
        await axios.post(
          `${BASE_URL}/books/borrow`,
          { book_id: id },
          { headers: { Authorization: `Bearer ${token}` } }
        )
        fetchBooks() // Refresh the book list after borrowing
      } catch (error) {
        console.error('Error borrowing the book:', error)
        alert('Failed to borrow the book. Please try again later.')
      } finally {
        borrowing.value[id] = false // Re-enable the button after the request completes
      }
    }

    onMounted(async () => {
      fetchBooks()
      await userStore.getUserProfile(), await userStore.borrowedBook()
    })

    return {
      books,
      borrowBook,
      borrowing
    }
  }
})
</script>
