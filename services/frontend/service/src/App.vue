<template>
  <div>
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
  export default {
    name: 'App',
    data: function () {
      return {
        index: 0,
        message: '',
        todos: [
          { id: this.index++, text: "First" },
          { id: this.index++, text: "Second" }
        ]
      }
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
