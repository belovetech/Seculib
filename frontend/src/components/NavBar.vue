<template>
  <nav v-if="showNavBar" class="bg-blue-600 text-white py-4 px-6">
    <div class="flex justify-between items-center">
      <h1 class="text-2xl font-bold">
        Seculib
        <img src="../assets/dark-logo.svg" alt="Logo" class="h-8 w-8 inline-block" />
      </h1>
      <button @click="toggleMobileMenu" class="sm:hidden focus:outline-none">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16m-7 6h7"
          />
        </svg>
      </button>
      <ul class="hidden sm:flex space-x-4">
        <!-- <li>
          <router-link
            to="/ddos-prevention-dashboard"
            class="hover:text-gray-300 transition-colors duration-300"
            v-if="showProfileLink"
            @click="closeMobileMenu"
          >
            Dashboard
          </router-link>
        </li> -->
        <template v-if="!isAdminPage">
          <li>
            <router-link
              to="/profile"
              class="hover:text-gray-300 transition-colors duration-300"
              v-if="showProfileLink"
              @click="closeMobileMenu"
            >
              Profile
            </router-link>
          </li>
          <li>
            <router-link
              to="/books"
              class="hover:text-gray-300 transition-colors duration-300"
              @click="closeMobileMenu"
            >
              Books
            </router-link>
          </li>
        </template>
        <li>
          <button
            class="hover:text-gray-300 transition-colors duration-300"
            @click="handleLogout"
            v-if="showProfileLink"
          >
            Logout
          </button>
        </li>
      </ul>
    </div>
    <ul v-if="isMobileMenuOpen" class="sm:hidden mt-4 space-y-4">
      <li>
        <router-link
          to="/profile"
          class="block text-center hover:text-gray-300 transition-colors duration-300"
          v-if="showProfileLink"
          @click="closeMobileMenu"
        >
          Profile
        </router-link>
      </li>
      <li>
        <router-link
          to="/books"
          class="block text-center hover:text-gray-300 transition-colors duration-300"
          @click="closeMobileMenu"
        >
          Books
        </router-link>
      </li>
      <li>
        <button
          class="block text-center hover:text-gray-300 transition-colors duration-300 w-full"
          @click="handleLogout"
          v-if="showProfileLink"
        >
          Logout
        </button>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import { defineComponent, computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/useUserStore'

export default defineComponent({
  name: 'NavBar',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const userStore = useUserStore()
    const isMobileMenuOpen = ref(false)

    const showNavBar = computed(() => {
      return !['/register', '/login', '/'].includes(route.path)
    })

    const showProfileLink = computed(() => {
      return !['/register', '/login', '/'].includes(route.path)
    })

    const isAdminPage = computed(() => {
      return route.path === '/admin'
    })

    const toggleMobileMenu = () => {
      isMobileMenuOpen.value = !isMobileMenuOpen.value
    }

    const closeMobileMenu = () => {
      isMobileMenuOpen.value = false
    }

    const handleLogout = () => {
      userStore.logout()
      router.push('/')
      closeMobileMenu()
    }

    return {
      isMobileMenuOpen,
      showNavBar,
      showProfileLink,
      isAdminPage,
      toggleMobileMenu,
      closeMobileMenu,
      handleLogout
    }
  }
})
</script>

<style scoped>
/* Add any additional styling if needed */
</style>
