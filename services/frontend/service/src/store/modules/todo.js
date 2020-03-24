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
      return state.lists.find(
        list => list.id === id
      )
    }
  },


  mutations: {
    addList: (state, list) => {
      state.lists.push(list)
    },

    addItemInListById: (state, payload) => {
      state.lists.find(
        list => list.id === payload.item.list
      ).items.push(payload.item)
    },

    deleteItem: (state, id) => {
      state.lists.forEach(element => {
        element.items = element.items.filter(
          item => item.id !== id
        )
      })
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
    },

    addedItemForList: (context, payload) => {
      API.post('/todo/items/', {
        list: payload.id, text: payload.text
      }).then(response => {
        context.commit('addItemInListById', {
          item: response.data
        })
      }).catch(error => {
        console.log(error)
      })
    },

    deleteItemById: (context, payload) => {
      API.delete(`/todo/items/${payload.id}/`).then(function() {
        context.commit('deleteItem', payload.id)
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}

export default TodoModule
