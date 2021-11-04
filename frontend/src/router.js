import { createRouter, createWebHistory } from 'vue-router'
// import Home from '../views/Home'
import Signin from '../views/Signin'
import MyPage from '../views/Mypage/'
import Register from '../views/Register'
import Memory from '../views/Mypage/Memory'

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
  },
]

const router  = createRouter({
  history: createWebHistory(),
  routes,
})

export default router