import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import home from '../pages/home'
import LocationCity from '../pages/LocationCity'
import SearchCity from '../pages/SearchCity'
import SearchMain from '../pages/SearchMain'
import user from '../pages/user'
import nearby from '../pages/nearby'
import discovery from '../pages/discovery'
import order from '../pages/order/order'
import login from '../pages/login'
import edit from '../pages/userInfo/edit'
import userInfo from '../pages/userInfo/index'
import trolley from '../pages/trolley/trolley'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/user',
      name: 'user',
      component: user
    },
    {
      path: '/nearby',
      name: 'nearby',
      component: nearby
    },
    {
      path: '/discovery',
      name: 'discovery',
      component: discovery
    },
    {
      path: '/order',
      name: 'order',
      component: order
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
      name: 'searchMain',
      component: SearchMain
    },
    {
      path: '/edit',
      name: 'edit',
      component: edit
    },
    {
      path: '/userInfo',
      name: 'userInfo',
      component: userInfo
    },
    {
      path: '/trolley',
      name: 'trolley',
      component: trolley
    }
  ]
})
