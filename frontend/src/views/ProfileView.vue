<template>
  <div class="flex justify-center items-center h-screen bg-gray-100 p-8">
    <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Your Profile</h2>

      <!-- <div v-if="loading" class="text-center text-gray-700">Loading profile...</div> -->

      <div class="space-y-6">
        <!-- Name -->
        <div class="bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-lg font-semibold text-gray-700">Name</h3>
          <p class="text-gray-900 text-xl mt-2">{{ profile.name }}</p>
        </div>

        <!-- Matric No -->
        <div class="bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-lg font-semibold text-gray-700">Matric No</h3>
          <p class="text-gray-900 text-xl mt-2">{{ profile.matric_no }}</p>
        </div>

        <!-- Department -->
        <div class="bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-lg font-semibold text-gray-700">Department</h3>
          <p class="text-gray-900 text-xl mt-2">{{ profile.department }}</p>
        </div>

        <!-- Level -->
        <div class="bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-lg font-semibold text-gray-700">Level</h3>
          <p class="text-gray-900 text-xl mt-2">{{ profile.level }}</p>
        </div>

        <div class="bg-gray-50 p-4 rounded-lg shadow-inner">
          <h3 class="text-lg font-semibold text-gray-700">BorrowedBook</h3>
          <p class="text-gray-900 text-xl mt-2">{{ borrowedBookData.count }}</p>
        </div>

        <!-- Buttons -->
        <div class="flex justify-between mt-8">
          <button
            @click="$router.push('/borrowed-books')"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg shadow focus:outline-none focus:shadow-outline w-full mr-2"
          >
            Borrowed Books
          </button>

          <button
            @click="goBack"
            class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-lg shadow focus:outline-none focus:shadow-outline w-full ml-2"
          >
            Go Back
          </button>
        </div>
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
