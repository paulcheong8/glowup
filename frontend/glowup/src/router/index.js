import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import AboutPage from '../pages/AboutPage.vue'
import Search from '../pages/Search.vue'
import Post from '../pages/Post.vue'
import Experiences from '../pages/Experiences.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/about',
    name: 'AboutPage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: AboutPage
  },
  {
    path: '/search', 
    name: 'Search', 
    component: Search
  },
  {
    path: '/post', 
    name: 'Post', 
    component: Post
  }, 
  {
    path: '/experiences', 
    name: 'Experiences', 
    component: Experiences
  },  

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
