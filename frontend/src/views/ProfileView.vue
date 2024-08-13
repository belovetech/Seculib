<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Student Profile</h2>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Name:</label>
        <p class="text-gray-900 text-lg font-medium">{{ profile.name }}</p>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Matric No:</label>
        <p class="text-gray-900 text-lg font-medium">{{ profile.matric_no }}</p>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Department:</label>
        <p class="text-gray-900 text-lg font-medium">{{ profile.department }}</p>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Level:</label>
        <p class="text-gray-900 text-lg font-medium">{{ profile.level }}</p>
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
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/useUserStore'

export default defineComponent({
  name: 'ProfileView',
  setup() {
    const profile = ref({
      name: '',
      matric_no: '',
      department: '',
      level: ''
    })
    const userStore = useUserStore()

    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1/students'

    const fetchProfile = async () => {
      console.log(`Bearer ${localStorage.getItem('token')}`)
      try {
        const response = await axios.get(`${BASE_URL}/profile`, {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
        const user = response.data.data
        profile.value = user
        userStore.currentUser(user)
      } catch (error) {
        console.error('Error fetching profile:', error)
      }
    }

    const goBack = () => {
      window.history.back()
    }

    onMounted(() => {
      fetchProfile()
    })

    return {
      profile,
      goBack
    }
  }
})
</script>

<style scoped>
/* Additional custom styles, if needed */
</style>
