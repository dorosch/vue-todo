<template>
  <ul>
    <h4>{{ list.title }}</h4>
    <TodoItem
      v-for="item in list.items"
      v-bind:key="item.id"
      v-bind:item="item"
    ></TodoItem>
  </ul>
</template>


<script>
  import TodoItem from './TodoItem'

  export default {
    name: 'TodoList',
    components: {
      TodoItem
    },
    props: [
      'list'
    ]
  }
</script>
