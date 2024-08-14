<template>
  <div class="flex justify-center h-screen bg-gray-100 p-8">
    <h2 class="text-3xl font-extrabold mb-8 text-center text-gray-800" >DDOS PLAYGROUND</h2>
    <!-- <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-4"> -->
    <!-- <p class="text-gray-800">DDOS display goes here</p> -->
    <!-- </div> -->
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'
import { useUserStore } from '@/stores/useUserStore'
import { computed } from 'vue'
import type { User } from '@/types'

export default defineComponent({
  name: 'PlayGround',
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
