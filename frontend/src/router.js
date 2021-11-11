import { createRouter, createWebHistory } from 'vue-router'
// import Home from '../views/Home'
import Signin from '../views/Signin'
import MyPage from '../views/Mypage/'
import Register from '../views/Register'
import Memory from '../views/Mypage/Memory'
import Table from '../views/Mypage/Table'
import Analytics from '../views/Mypage/Analytics'
import Settings from '../views/Mypage/Settings'

const routes = [
  {
    path: '/',
    redirect: '/login'
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
    props: true,
  },
  {
    path: '/mypage/memory',
    name: 'Memory',
    component: Memory,
    props: true,
  },
  {
    path: '/mypage/table',
    name: 'Table',
    component: Table,
    props: true,
  },
  {
    path: '/mypage/analytics',
    name: 'Analytics',
    component: Analytics,
    props: true,
  },
  {
    path: '/mypage/settings',
    name: 'Settings',
    component: Settings,
    props: true,
  }
]

const router  = createRouter({
  history: createWebHistory(),
  routes,
})

export default router