<template>
  <li>
    {{ item.text }}
    <button v-on:click="deleteItem">Delete</button>
  </li>
</template>


<script>
  export default {
    name: 'TodoItem',
    props: {
      item: Object
    },
    methods: {
      deleteItem: function() {
        this.$store.dispatch('deleteItemById', {
          id: this.item.id
        })
      }
    }
  }
</script>
