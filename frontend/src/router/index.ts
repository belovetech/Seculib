import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import BookListView from '../components/BookList.vue'
import ProfileView from '../views/ProfileView.vue'
import BorrowedBooksView from '../views/BorrowedBooksView.vue'
import AdminView from '../views/AdminView.vue'
// import DashBoardView from '../views/DashBoardView.vue'
import { useUserStore } from '@/stores/useUserStore'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/books',
    name: 'Books',
    component: BookListView,
    meta: { requiresAuth: true }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true }
  },
  {
    path: '/borrowed-books',
    name: 'BorrowedBooks',
    component: BorrowedBooksView,
    meta: { requiresAuth: true }
  },
  {
    path: '/admin',
    name: 'Admin',
    component: AdminView,
    // meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()

  // Check if the route requires authentication
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // If the user is not logged in, redirect to the login page
    if (!userStore.isUserAuthenticated) {
      next({ name: 'Login' })
    } else {
      next() // Proceed to the route
    }
  } else {
    next() // Proceed to the route
  }
})

export default router
