<template>
  <div class="p-8 bg-gray-100 min-h-screen">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Admin Dashboard</h1>

    <div v-if="isLoading" class="text-center text-gray-600">
      Loading statistics...
    </div>

    <div v-else-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-6" role="alert">
      <strong class="font-bold">Error!</strong>
      <span class="block sm:inline">{{ error }}</span>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <!-- User Statistics -->
      <div class="bg-white shadow-lg rounded-lg p-6 transition-all duration-300 hover:shadow-xl">
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center">
            <i class="fas fa-users text-blue-500 text-2xl mr-3"></i>
            <h2 class="text-xl font-semibold text-gray-700">User Statistics</h2>
          </div>
        </div>
        <div class="space-y-4">
          <div class="flex justify-between items-center">
            <h3 class="text-lg text-gray-600">Admins</h3>
            <p class="text-2xl font-bold text-blue-500">{{ statistics.admins }}</p>
          </div>
          <div class="flex justify-between items-center">
            <h3 class="text-lg text-gray-600">Logged In Users</h3>
            <p class="text-2xl font-bold text-purple-500">{{ statistics.logged_in_users }}</p>
          </div>
        </div>
      </div>

      <!-- Book Inventory -->
      <div class="bg-white shadow-lg rounded-lg p-6 transition-all duration-300 hover:shadow-xl">
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center">
            <i class="fas fa-book text-green-500 text-2xl mr-3"></i>
            <h2 class="text-xl font-semibold text-gray-700">Book Inventory</h2>
          </div>
        </div>
        <div class="space-y-4">
          <div class="flex justify-between items-center">
            <h3 class="text-lg text-gray-600">Available Books</h3>
            <p class="text-2xl font-bold text-green-500">{{ statistics.available_books }}</p>
          </div>
          <div class="flex justify-between items-center">
            <h3 class="text-lg text-gray-600">Borrowed Books</h3>
            <p class="text-2xl font-bold text-red-500">{{ statistics.borrowed_books }}</p>
          </div>
        </div>
      </div>

      <!-- Security Alerts -->
      <div class="bg-white shadow-lg rounded-lg p-6 transition-all duration-300 hover:shadow-xl">
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center">
            <i class="fas fa-shield-alt text-yellow-500 text-2xl mr-3"></i>
            <h2 class="text-xl font-semibold text-gray-700">Security Alerts</h2>
          </div>
        </div>
        <div class="space-y-4">
          <div class="flex justify-between items-center">
            <h3 class="text-lg text-gray-600">Suspicious DDoS</h3>
            <p class="text-2xl font-bold text-yellow-500">
              {{ statistics.ddos_attack.suspicious_ddos_attack }}
            </p>
          </div>
          <div class="flex justify-between items-center">
            <h3 class="text-lg text-gray-600">Potential DDoS</h3>
            <p class="text-2xl font-bold text-teal-500">
              {{ statistics.ddos_attack.possible_ddos_attack }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Chart Section -->
    <div class="bg-white shadow-md rounded-lg p-6">
      <h2 class="text-xl font-semibold text-gray-600 mb-4">User Request Statistics</h2>
      <canvas id="requestsChart"></canvas>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Chart, registerables } from 'chart.js'
import axios from 'axios'

Chart.register(...registerables)

const statistics = ref({
  admins: 0,
  available_books: 0,
  borrowed_books: 0,
  logged_in_users: 0,
  students: 0,
  requests: {
    authenticated_user_requests: 0,
    unauthenticated_user_requests: 0
  },
  ddos_attack: {
    possible_ddos_attack: false,
    suspicious_ddos_attack: 0
  }
})

const error = ref('')
const isLoading = ref(false)

onMounted(() => {
  getStatistics()
})

function getStatistics() {
  const token = localStorage.getItem('token')
  isLoading.value = true
  error.value = ''

  axios
    .get('https://secure-auth-dos-prevention.onrender.com/api/v1/admin/statistics', {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then((response) => {
      console.log(response.data.data)
      statistics.value = response.data.data
      renderChart()
    })
    .catch((error) => {
      console.error('Error fetching statistics:', error)
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        error.value = `Server error: ${error.response.status} - ${error.response.data.message || 'Unknown error'}`
      } else if (error.request) {
        // The request was made but no response was received
        error.value = 'Network error: No response received from server'
      } else {
        // Something happened in setting up the request that triggered an Error
        error.value = `Error: ${error.message}`
      }
    })
    .finally(() => {
      isLoading.value = false
    })
}

function renderChart() {
  const ctx = document.getElementById('requestsChart') as HTMLCanvasElement
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Authenticated', 'Unauthenticated'],
      datasets: [
        {
          label: 'Requests',
          data: [
            statistics.value.requests.authenticated_user_requests,
            statistics.value.requests.unauthenticated_user_requests
          ],
          backgroundColor: ['#4FD1C5', '#F6E05E']
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  })
}
</script>

<style>
body {
  font-family: 'Inter', sans-serif;
}
</style>
