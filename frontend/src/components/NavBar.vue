<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/useUserStore'

export default defineComponent({
  name: 'NavBar',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const userStore = useUserStore()

    const showNavBar = computed(() => {
      return !['/register', '/login', '/'].includes(route.path)
    })

    const showProfileLink = computed(() => {
      return !['/register', '/login', '/'].includes(route.path)
    })

    const logout = () => {
      userStore.logout()
      router.push('/')
    }

    return {
      logout,
      showNavBar,
      showProfileLink
    }
  }
})
</script>

<style scoped>
/* Add any additional styling if needed */
</style>

<template>
  <nav v-if="showNavBar" class="bg-blue-600 text-white py-4 px-6 flex justify-between items-center">
    <h1 class="text-2xl font-bold">
      Seculib
      <img src="../assets/dark-logo.svg" alt="Logo" class="h-8 w-8 inline-block" />
    </h1>
    <ul class="flex space-x-4">
      <li>
        <router-link to="/profile" class="hover:text-gray-300" v-if="showProfileLink">
          Profile
        </router-link>
      </li>
      <li>
        <router-link to="/books" class="hover:text-gray-300">Books</router-link>
      </li>
      <li>
        <button class="hover:text-gray-300" @click="logout" v-if="showProfileLink">Logout</button>
      </li>
    </ul>
  </nav>
</template>
