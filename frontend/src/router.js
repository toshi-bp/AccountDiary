import { createRouter, createWebHistory } from 'vue-router'

import Signin from '../views/Signin'
import MyPage from '../views/Mypage/'
import Register from '../views/Register'
import Memory from '../views/Mypage/Memory'
import Table from '../views/Mypage/Table'
import Settings from '../views/Mypage/Settings'
import Analytics from '../views/Mypage/Analytics'

const routes = [
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
  },
  {
    path: '/mypage/memory',
    name: 'Memory',
    component: Memory,
  },
  {
    path: '/mypage/table',
    name: 'Table',
    component: Table,
  },
  {
    path: '/mypage/settings',
    name: 'Settings',
    component: Settings,
  },
  {
    path: '/mypage/analytics',
    name: 'Analytics',
    component: Analytics,
  }
]

const router  = createRouter({
  history: createWebHistory(),
  routes,
})

export default router