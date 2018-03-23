<template>
  <nav class="tabs is-fullwidth">
  	<div class="columns is-mobile is-gapless">
		<!-- <ul> -->
		<div class="column is-4 mediumFont">
		  <router-link tag="li" activeClass='is-active' :to="{ path: 'one'}"><a>Explore Map</a></router-link>
		</div>
		<div class="column is-4 mediumFont">
		  <router-link tag="li" activeClass='is-active' :to="{ path: 'two'}"><a>Pricing Sku</a></router-link>
		</div>
		<div class="column is-4 mediumFont">
		  <router-link tag="li" activeClass='is-active' :to="{ path: 'two'}"><a>Explore Dataset</a></router-link>
		</div>
		<div class="column is-1 mediumFont">
		  <router-link tag="li" activeClass='is-active' :to="{ path: 'two'}"><a>Info</a></router-link>
		</div>
		<!-- </ul> -->
	</div>
  </nav>
</template>

<script>
export default {
  name: 'SubNavbar'
}
</script>

<style lang="sass" scoped>

.tabs
	background-color: darken($background, 2)

</style>
