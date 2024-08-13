<template>
  <div class="py-10">
    <h2 class="text-2xl font-bold mb-6">Available Books</h2>
    <ul>
      <li v-for="book in books" :key="book.id" class="mb-4">
        <h3 class="text-xl">{{ book.title }}</h3>
        <p>{{ book.author }}</p>
        <button @click="borrowBook(book.id)" class="bg-green-500 text-white py-1 px-4 rounded">
          Borrow
        </button>
        <button
          v-if="book.borrowed"
          @click="returnBook(book.id)"
          class="bg-red-500 text-white py-1 px-4 rounded ml-2"
        >
          Return
        </button>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/useUserStore'

interface Book {
  id: number
  title: string
  author: string
  borrowed: boolean
}

export default defineComponent({
  name: 'BookList',
  setup() {
    const books = ref<Book[]>([])
    const userStore = useUserStore()

    const fetchBooks = async () => {
      if (!userStore.isAuthenticated) {
        // Handle unauthenticated access
        return
      }

      try {
        const response = await axios.get<Book[]>('your-backend-api/books')
        books.value = response.data
      } catch (error) {
        // Handle error
      }
    }

    const borrowBook = async (id: number) => {
      if (!userStore.isAuthenticated) {
        // Handle unauthenticated action
        return
      }

      try {
        await axios.post(`your-backend-api/borrow/${id}`)
        fetchBooks()
      } catch (error) {
        // Handle error
      }
    }

    const returnBook = async (id: number) => {
      if (!userStore.isAuthenticated) {
        // Handle unauthenticated action
        return
      }

      try {
        await axios.post(`your-backend-api/return/${id}`)
        fetchBooks()
      } catch (error) {
        // Handle error
      }
    }

    onMounted(fetchBooks)

    return {
      books,
      borrowBook,
      returnBook
    }
  }
})
</script>
