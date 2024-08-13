import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import BookListView from '../components/BookList.vue'
import ProfileView from '../views/ProfileView.vue'
import BorrowedBooksView from '../views/BorrowedBooksView.vue'

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
    component: BookListView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/borrowed-books',
    name: 'BorrowedBooks',
    component: BorrowedBooksView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
