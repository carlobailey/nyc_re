<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="bigFont cleanBorder" id="titleBlock">
        <!-- Open NYC house price model -->
        Open Source NYC Real Estate
      </a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <span class="navbar-item is-size-7 is-dark">{{version}}</span>
      </div>
    </div>
  </nav>
</template>
<script>

export default {
  name: 'Navbar',
  data () {
    return {
      version: this.$store.state.version
    }
  }
}
</script>

<style lang="sass" scoped>

nav.navbar
  min-height: none
  background-color: $nav-background
  border-bottom: solid 1px #dbdbdb

.navbar-brand > .navbar-item
  padding-left: 10px

  img
    height: 15px

</style>
