<template>
  <div class="flex flex-col justify-center items-center min-h-screen bg-gray-900 text-center">
    <h1 class="text-2xl sm:text-3xl md:text-4xl font-bold text-white">
      Seculib DDOS Attack Test
      <img
        src="../assets/white-logo.svg"
        alt="Logo"
        class="h-10 w-10 sm:h-12 sm:w-12 inline-block ml-2"
      />
    </h1>
    <p class="mt-4 text-gray-300 sm:text-lg">
      This is a test page to test the ddos protection of the backend.
    </p>
    <div class="mt-8 flex flex-col sm:flex-row gap-4">
      <button
        @click="launchDDOSAttackOnBackend"
        :disabled="launching"
        class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        {{ launching ? 'Launching...' : 'Launch DDOS Attack' }}
      </button>
    </div>
    <p v-if="attackLaunched && !launching" class="text-red-500 mt-4">
      Attack launched successfully
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import axios, { AxiosError } from 'axios'

export default defineComponent({
  name: 'DdosTestView',
  setup() {
    const launching = ref(false)
    const attackLaunched = ref(false)

    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1'

    const launchDDOSAttackOnBackend = async () => {
      try {
        launching.value = true
        await axios.get(`${BASE_URL}/books`)
        launching.value = false
        attackLaunched.value = true
      } catch (e) {
        const error = e as AxiosError
        console.error('statuscode: ', error.response?.status)
        launching.value = false
        attackLaunched.value = false
      }
    }

    return {
      launchDDOSAttackOnBackend,
      launching,
      attackLaunched
    }
  }
})
</script>
