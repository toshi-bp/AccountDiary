import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home'
import Signin from '../views/Signin'
import MyPage from '../views/Mypage/'
import Register from '../views/Register'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Signin,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/mypage',
    name: 'MyPage',
    component: MyPage,
  }
]

const router  = createRouter({
  history: createWebHistory(),
  routes,
})

export default router