<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Your Profile</h2>

      <div v-if="loading" class="text-center text-gray-700">Loading profile...</div>

      <div v-else class="space-y-6">
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

<style scoped>
/* Additional custom styles, if needed */
</style>
