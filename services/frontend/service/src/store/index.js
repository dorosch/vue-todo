import Vue from 'vue'
import Vuex from 'vuex'

import TodoModule from './modules/todo'


Vue.use(Vuex)

const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    todo: TodoModule
  }
})

export default store
