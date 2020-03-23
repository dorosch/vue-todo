import API from '../../api/http'


const TodoModule = {
  state: {
    lists: []
  },
  getters: {
    getLists: state => {
      return state.lists
    },
    getListById: state => id => {
      return state.lists.find(list => list.id === id)
    }
  },
  mutations: {
    addList: (state, list) => {
      state.lists.push(list)
    }
  },
  actions: {
    fetchLists: (context) => {
      API.get('/todo/lists/').then(response => {
        response.data.forEach(
          element => context.commit('addList', element)
        )
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}

export default TodoModule
