import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import home from '../pages/home'
import LocationCity from '../pages/LocationCity'
import SearchCity from '../pages/SearchCity'
import SearchMain from '../pages/SearchMain'
import login from '../pages/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/locationCities',
      name: 'locationCities',
      component: LocationCity
    },
    {
      path: '/searchCity',
      name: 'searchCity',
      component: SearchCity
    },
    {
      path: '/searchMain',
      name: '/searchMain',
      component: SearchMain
    }
  ]
})
