<template>
  <div>
    <TodoList
      v-for="list in lists"
      v-bind:key="list.id"
      v-bind:list="list"
    ></TodoList>
  </div>
</template>


<script>
  import API from '../../api/http'
  import TodoList from './TodoList'

  export default {
    name: 'Todo',
    components: {
      TodoList
    },
    data: function () {
      return {
        lists: []
      }
    },
    mounted: function () {
      API.get('/todo/lists/').then(response => {
        this.lists = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
</script>
