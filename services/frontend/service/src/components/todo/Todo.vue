<template>
  <div class="lists">
    <TodoList
      v-for="list in lists"
      v-bind:key="list.id"
      v-bind:list="list"
    ></TodoList>
  </div>
</template>


<script>
  import TodoList from './TodoList'

  export default {
    name: 'Todo',
    components: {
      TodoList
    },
    computed: {
      lists: function() {
        return this.$store.getters.getLists
      }
    },
    mounted: function () {
      this.$store.dispatch('fetchLists')
    }
  }
</script>


<style>
  .lists {
    display: grid;
    grid-auto-columns: 272px;
    grid-auto-flow: column;
    grid-gap: 8px;
    overflow: scroll;
    margin: 10px;
  }
</style>
