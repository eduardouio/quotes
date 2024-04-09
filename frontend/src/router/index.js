import { createRouter, createWebHistory } from 'vue-router'
import QuotesView from '../views/QuotesView.vue'
import ProfileView from '../views/ProfileView.vue'
import ReportView from '../views/ReportView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: QuotesView
    }
  ]
})
export default router
