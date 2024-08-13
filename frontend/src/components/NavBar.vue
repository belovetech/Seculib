<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useRoute } from 'vue-router'

export default defineComponent({
  name: 'NavBar',
  setup() {
    const route = useRoute()

    const showNavBar = computed(() => {
      return !['/register', '/login', '/'].includes(route.path)
    })

    const showProfileLink = computed(() => {
      return !['/register', '/login'].includes(route.path)
    })

    return {
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
      SecureLib
      <img src="../assets/dark-logo.svg" alt="Logo" class="h-8 w-8 inline-block" />
    </h1>
    <ul class="flex space-x-4">
      <li>
        <router-link to="/" class="hover:text-gray-300" v-if="showProfileLink"> Home </router-link>
      </li>
      <li>
        <router-link to="/profile" class="hover:text-gray-300" v-if="showProfileLink">
          Profile
        </router-link>
      </li>
      <li>
        <router-link to="/books" class="hover:text-gray-300">Books</router-link>
      </li>
      <!-- Add other navigation links here -->
    </ul>
  </nav>
</template>
