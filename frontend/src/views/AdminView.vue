<template>
  <div class="p-8 bg-gray-100 min-h-screen">
    <!-- Page Header -->
    <h1 class="text-3xl font-bold mb-6 text-gray-700">Admin Dashboard</h1>

    <!-- Statistics Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div class="bg-white shadow-md rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-600">Admins</h2>
        <p class="text-3xl font-bold text-blue-500">{{ statistics.admins }}</p>
      </div>
      <div class="bg-white shadow-md rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-600">Available Books</h2>
        <p class="text-3xl font-bold text-green-500">{{ statistics.available_books }}</p>
      </div>
      <div class="bg-white shadow-md rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-600">Borrowed Books</h2>
        <p class="text-3xl font-bold text-red-500">{{ statistics.borrowed_books }}</p>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div class="bg-white shadow-md rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-600">Logged In Users</h2>
        <p class="text-3xl font-bold text-purple-500">{{ statistics.logged_in_users }}</p>
      </div>
      <div class="bg-white shadow-md rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-600">Authenticated Requests</h2>
        <p class="text-3xl font-bold text-teal-500">
          {{ statistics.requests.authenticated_user_requests }}
        </p>
      </div>
      <div class="bg-white shadow-md rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-600">Unauthenticated Requests</h2>
        <p class="text-3xl font-bold text-yellow-500">
          {{ statistics.requests.unauthenticated_user_requests }}
        </p>
      </div>
    </div>

    <!-- Chart Section -->
    <div class="bg-white shadow-md rounded-lg p-6">
      <h2 class="text-xl font-semibold text-gray-600 mb-4">User Request Statistics</h2>
      <canvas id="requestsChart"></canvas>
    </div>
  </div>
</template>
<!--
<script lang="ts">
import { Chart } from 'chart.js'

export default {
  data() {
    return {
      statistics: {
        admins: 1,
        available_books: 15,
        borrowed_books: 0,
        logged_in_users: 2,
        requests: {
          authenticated_user_requests: 2,
          unauthenticated_user_requests: 7
        },
        students: 1
      }
    }
  },
  mounted() {
    this.renderChart()
  },
  methods: {
    renderChart() {
      const ctx = document.getElementById('requestsChart').getContext('2d')
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Authenticated', 'Unauthenticated'],
          datasets: [
            {
              label: 'Requests',
              data: [
                this.statistics.requests.authenticated_user_requests,
                this.statistics.requests.unauthenticated_user_requests
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
  }
}
</script> -->

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const statistics = ref({
  admins: 1,
  available_books: 15,
  borrowed_books: 0,
  logged_in_users: 2,
  requests: {
    authenticated_user_requests: 2,
    unauthenticated_user_requests: 7
  },
  students: 1
})

onMounted(() => {
  renderChart()
})

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
