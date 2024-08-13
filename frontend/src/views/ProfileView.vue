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
    const loading = ref(true) // Loading state
    const userStore = useUserStore()
    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1/students'

    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem('token')
        if (!token) throw new Error('Token not found')

        const response = await axios.get(`${BASE_URL}/profile`, {
          headers: { Authorization: `Bearer ${token}` }
        })

        profile.value = response.data.data
        userStore.currentUser(response.data.data)
      } catch (error) {
        alert('Unable to fetch profile')
        console.error('Error fetching profile:', error)
      } finally {
        loading.value = false // Set loading to false after data is fetched
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
      loading,
      goBack
    }
  }
})
</script>

<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Student Profile</h2>

      <!-- Loading Indicator -->
      <div v-if="loading" class="text-center text-gray-700">Loading profile...</div>

      <!-- Profile Content -->
      <div v-else>
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
  </div>
</template>

<style scoped>
/* Additional custom styles, if needed */
</style>
