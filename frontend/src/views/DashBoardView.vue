<!-- DDoS Prevention Dashboard -->
<template>
  <div class="flex justify-center items-start min-h-screen bg-gray-100 p-4 sm:p-12">
    <div class="w-full max-w-4xl bg-white shadow-lg rounded-lg p-6 sm:p-8">
      <div class="min-w-full flex justify-between items-center">
        <span class="text-2xl sm:text-3xl font-extrabold mb-6 text-gray-800">
          DDoS Attack Logs
        </span>
        <button
          @click="launchDDOSAttack()"
          :disabled="attacking"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          {{ attacking ? 'Attacking...' : 'Attack' }}
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="min-w-full bg-white border border-gray-200">
          <thead class="bg-gray-700">
            <tr>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">IP Address</th>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">Attempt Date</th>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">Attack Type</th>
              <th class="py-3 px-4 text-left text-white border-b border-gray-200">Request Count</th>
              <th class="py-3 px-4 text-center text-white border-b border-gray-200">Status</th>
            </tr>
          </thead>
          <tbody class="text-gray-600">
            <tr
              v-for="attempt in ddosAttemptList"
              :key="attempt.id"
              class="border-t border-gray-200 hover:bg-gray-100"
            >
              <td class="py-3 px-4">{{ attempt.ip_address }}</td>
              <td class="py-3 px-4">{{ formatDate(attempt.attempt_date) }}</td>
              <td class="py-3 px-4">{{ attempt.attack_type }}</td>
              <td class="py-3 px-4">{{ attempt.request_count }}</td>
              <td class="py-3 px-4 text-center">{{ attempt.status }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { useUserStore } from '@/stores/useUserStore'
import type { DDOSAttempt } from '@/types'
import { ddosAttempts } from '@/stores/data'

export default defineComponent({
  name: 'BorrowedBooksView',
  setup() {
    const attacking = ref(false)
    const userStore = useUserStore()
    const ddosAttemptList = ref<DDOSAttempt[]>(ddosAttempts)

    // const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1'

    const launchDDOSAttack = async () => {
      if (attacking.value) return

      attacking.value = true
      return 'attack launched'
    }

    const formatDate = (dateString: string) => {
      const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(dateString).toLocaleDateString(undefined, options)
    }

    const goBack = () => {
      window.history.back()
    }

    onMounted(async () => {
      await userStore.borrowedBook()
    })

    return {
      goBack,
      formatDate,
      launchDDOSAttack,
      ddosAttemptList,
      attacking
    }
  }
})
</script>
