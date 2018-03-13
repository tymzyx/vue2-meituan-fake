import Vue from 'vue'
import Vuex from 'vuex'

import mutations from './mutations'

Vue.use(Vuex)

const state = {
  selectedCity: '', // 当前城市，用户可自由选择
  locatedCity: '', // 定位所在城市
  recentCities: [], // 保存最近访问的两座城市
  username: '', // 用户名
}

const store = new Vuex.Store({
  state,
  mutations
})

export default store

