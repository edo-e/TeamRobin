<script>
	import { select, selectAll } from "d3-selection";
	import { axisBottom, axisLeft } from "d3-axis";
	export let y;
	export let scale;
	let transform;
	let g;
	$: {
		select(g).selectAll("*").remove();
		let Axis = axisBottom(scale);
		transform = `translate(0, ${y})`;
		select(g).call(Axis);
	}
</script>

<g class="Axis" bind:this={g} {transform} />
