import { reactive, readonly } from "vue";

const state = reactive({
  userId: ''
})

const mutations = {
  setUserId(state, loginUser) {
    state.userId = loginUser
  }
}

const actions = {
  setUserId: ({ commit }) => commit("setUserId")
}

export default {
  state: readonly(state),
  setUserId
}

export const key = Symbol('key')