<template>
  <div>
    <input
      v-focus
      v-model="data"
      v-on:keyup.enter="inputData"
    />
    <button
      v-if="data.length >= 1"
      @mousedown="inputData"
    >
      {{ buttonText }}
    </button>
  </div>
</template>


<script>
  export default {
    name: 'InlineInput',
    props: {
      callback: Function,
      buttonText: String
    },
    data: function() {
      return {
        data: ''
      }
    },
    methods: {
      inputData: function() {
        if (typeof this.callback == 'function') {
          this.callback(this.data)
        }
        else {
          console.error('`callback` must be a function')
        }
      }
    },
    directives: {
      focus: {
        inserted: function (el) {
          el.focus()
        }
      }
    }
  }
</script>
