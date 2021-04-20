<script>
	export let name;

	import Papa from "papaparse";
	import { scaleLinear } from "d3-scale";
	import { min, max } from "d3-array";
	import Axis from './Axis.svelte';


	const MARGIN = { LEFT: 5, RIGHT: 5, TOP: 5, BOTTOM: 5 };
	const WIDTH = 400 - MARGIN.LEFT - MARGIN.RIGHT;
	const HEIGHT = 600 - MARGIN.TOP - MARGIN.BOTTOM;

	let raw_data = [];
	Papa.parse("cars.csv", {
		header: true,
		download: true,
		complete: function (results) {
			raw_data = results.data;
		},
	});
	let datapoints = [];
	$: {
		raw_data.forEach((d) => {
			datapoints = [
				...datapoints,
				{
					name: d.name,
					sixty: Number(d.sixty),
					displacement: +d.displacement,
					power: +d.power,
					economy: +d.economy,
					cylinders: +d.cylinders,
					weight: +d.weight,
					year: +d.year,
				},
			];
		});
	}

	$: scale_weight = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.weight;
				})
			),
			max(
				datapoints.map((d) => {
					return d.weight;
				})
			),
		])
		.range([0, WIDTH]);

	$: scale_economy = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.economy;
				})
			),
			max(
				datapoints.map((d) => {
					return d.economy;
				})
			),
		])
		.range([0, WIDTH]);

	$: scale_power = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.power;
				})
			),
			max(
				datapoints.map((d) => {
					return d.power;
				})
			),
		])
		.range([0, WIDTH]);

	$: scale_cylinders = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.cylinders;
				})
			),
			max(
				datapoints.map((d) => {
					return d.cylinders;
				})
			),
		])
		.range([0, WIDTH]);

	$: scale_displacement = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.displacement;
				})
			),
			max(
				datapoints.map((d) => {
					return d.displacement;
				})
			),
		])
		.range([0, WIDTH]);

	$: scale_year = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.year;
				})
			),
			max(
				datapoints.map((d) => {
					return d.year;
				})
			),
		])
		.range([0, WIDTH]);

	$: scale_sixty = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.sixty;
				})
			),
			max(
				datapoints.map((d) => {
					return d.sixty;
				})
			),
		])
		.range([0, WIDTH]);

	$: color_scale = scaleLinear()
		.domain([
			min(
				datapoints.map((d) => {
					return d.weight;
				})
			),
			max(
				datapoints.map((d) => {
					return d.weight;
				})
			),
		])
		.range(["green", "brown"]);

	const lineGenerator = function (d) {
		return (
			"M " +
			scale_economy(d.economy) +
			" 0 " +
			" L " +
			scale_cylinders(d.cylinders) +
			" 100 " +
			" L " +
			scale_displacement(d.displacement) +
			" 200 " +
			" L " +
			scale_power(d.power) +
			" 300 " +
			" L " +
			scale_weight(d.weight) +
			" 400 " +
			" L " +
			scale_sixty(d.sixty) +
			" 500 " +
			" L " +
			scale_year(d.year) +
			" 600 "
		);
	};

</script>

<svg width={WIDTH.toString()} height={HEIGHT.toString()}>
	
	<Axis y={0} scale={scale_economy} />
	<Axis y={100} scale={scale_cylinders} />
	<Axis y={200} scale={scale_displacement} />
	<Axis y={300} scale={scale_power} />
	<Axis y={400} scale={scale_weight} />
	<Axis y={500} scale={scale_sixty} />
	<Axis y={HEIGHT-10} scale={scale_year} />

	{#each datapoints as datapoint}
		<path
			d={lineGenerator(datapoint)}
			style="stroke: {color_scale(datapoint.weight)}"
		/>
	{/each}
</svg>

<style>
	svg {
		background-color: whitesmoke;
		padding: 10px;
	}
	path {
		stroke: black;
		fill: none;
		opacity: 0.5;
	}
	path:hover {
		stroke: tomato;
		opacity: 1;
		stroke-width: 3;
	}
	line {
		stroke: black;
		opacity: 0.8;
	}
</style>
