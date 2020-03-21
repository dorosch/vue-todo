<template>
  <div>
    <p v-if="errors.length">
      <ol>
        <ul v-for="error in errors" v-bind:key="error.message">
          {{ error.name }}: {{ error.message }}
        </ul>
      </ol>
    </p>
    <input v-model="message" placeholder="edit me">
    <button v-on:click="addTodo">Click</button>
    <ol>
      <li v-for="todo in todos" v-bind:key="todo.id">
        {{ todo.text }}
        <button v-on:click="delTodo(todo)">X</button>
      </li>
    </ol>
  </div>
</template>


<script>
  import API from './http'

  export default {
    name: 'App',
    data: function () {
      return {
        index: 0,
        message: '',
        todos: [],
        errors: []
      }
    },
    mounted: function () {
      API.get('/todo/lists/1/').then(response => {
        this.todos = response.data.items
      })
      .catch(error => {
        this.errors.push(error)
      })
    },
    methods: {
      addTodo: function() {
        if (this.message)
          this.todos.push({id: this.index++, text: this.message})
      },
      delTodo: function(todo) {
        this.index--
        this.todos.splice(todo.id, 1)
      }
    }
  }
</script>
