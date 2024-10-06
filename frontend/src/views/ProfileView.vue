<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-4 sm:p-12">
    <div class="w-full max-w-4xl bg-white shadow-lg rounded-lg p-6 sm:p-8">
      <!-- <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Details</h2> -->
      <h2 class="text-xl font-bold mb-6 text-center text-gray-800">Details</h2>

      <!-- Profile Information Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <!-- Name -->
        <div class="flex justify-between bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-sm sm:text-lg font-semibold text-gray-700">Name:</h3>
          <p class="text-gray-900 text-sm sm:text-lg">{{ profile.name }}</p>
        </div>

        <!-- Matric No -->
        <div class="flex justify-between bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-sm sm:text-lg font-semibold text-gray-700">Matric No:</h3>
          <p class="text-gray-900 text-sm sm:text-lg">{{ profile.matric_no }}</p>
        </div>

        <!-- Department -->
        <div class="flex justify-between bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-sm sm:text-lg font-semibold text-gray-700">Department:</h3>
          <p class="text-gray-900 text-sm sm:text-lg">{{ profile.department }}</p>
        </div>

        <!-- Level -->
        <div class="flex justify-between bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-sm sm:text-lg font-semibold text-gray-700">Level:</h3>
          <p class="text-gray-900 text-sm sm:text-lg">{{ profile.level }}</p>
        </div>

        <!-- Borrowed Book Count -->
        <div class="flex justify-between bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-sm sm:text-lg font-semibold text-gray-700">Borrowed Books:</h3>
          <p class="text-gray-900 text-sm sm:text-lg">{{ borrowedBookData.count }}</p>
        </div>
      </div>

      <!-- Buttons -->
      <div
        class="flex flex-col sm:flex-row justify-between mt-8 space-y-4 sm:space-y-0 sm:space-x-4"
      >
        <button
          @click="$router.push('/borrowed-books')"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg shadow focus:outline-none focus:shadow-outline w-full"
        >
          View Borrowed Books
        </button>

        <button
          @click="goBack"
          class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-lg shadow focus:outline-none focus:shadow-outline w-full"
        >
          Go Back
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'
import { useUserStore } from '@/stores/useUserStore'
import { computed } from 'vue'
import type { User } from '@/types'

export default defineComponent({
  name: 'ProfileView',
  setup() {
    const userStore = useUserStore()
    const user: User = {
      department: '',
      id: 0,
      level: '',
      matric_no: '',
      name: ''
    }

    const profile = computed(() => {
      return userStore.user ?? user
    })

    const borrowedBookData = computed(() => {
      return userStore.borrowedBooks
    })

    const goBack = () => {
      window.history.back()
    }

    onMounted(async () => {
      await userStore.getUserProfile()
      await userStore.borrowedBook()
    })

    return {
      profile,
      borrowedBookData,
      goBack
    }
  }
})
</script>

<style scoped>
/* Additional custom styles, if needed */
</style>
