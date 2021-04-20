<script>
    import { scaleLog, scaleOrdinal, scaleLinear } from "d3-scale";
    import { schemeCategory10 } from "d3-scale-chromatic";
    import { selectAll, select } from "d3-selection";
    import { min, max } from "d3-array";
    import { transition_out } from "svelte/internal";
    //import  Dotting, { filename } from './App.svelte';

    const WIDTH = 1400;
    const HEIGHT = 1800;

    export let datapoints = [];
    export let target_dotting = [];
    export let filename_dotting = [];

    const radius = function (d) {
        if (
            (scale_r_dest(d) > 0) &
            (filename_dotting == "Total_destination.csv")
        ) {
            return scale_r_dest(d);
        } else if (
            (scale_r_cont(d) > 0) &
            (filename_dotting == "Total_continent.csv")
        ) {
            return scale_r_cont(d);
        } else if (
            (scale_r_ori(d) > 0) &
            (filename_dotting == "Total_origin.csv")
        ) {
            return scale_r_ori(d);
        } else return 1;
    };

    const continentColor = scaleOrdinal(schemeCategory10);
    $: scale_r_ori = scaleLinear().domain([5, 35974445]).range([5, 50]);
    $: scale_r_dest = scaleLinear().domain([5, 128209596]).range([5, 50]);
    $: scale_r_cont = scaleLinear().domain([0, 216307703]).range([5, 250]);
</script>

<svg id="svg1" width={WIDTH.toString()} height={HEIGHT.toString()}>
    {#each datapoints as datapoint}
        <circle
            cx={datapoint.X}
            cy={datapoint.Y}
            r={radius(datapoint.Female)}
            fill={continentColor(datapoint.Continent)}
            transition_in:fade={{ delay: 3000 }}
            transition_out:fade={{ delay: 3000 }}
        />
        <circle
            cx={datapoint.X}
            cy={datapoint.Y}
            r={radius(datapoint.Male)}
            stroke="black"
            fill="none"
        />

        <text x={datapoint.X} y={datapoint.Y} text-anchor="middle"
            >{datapoint[target_dotting]}</text
        >
    {/each}
</svg>

<style>
    text {
        opacity: 0.01;
        font: 15px Arial, sans-serif;
    }
    text:hover {
        opacity: 0.9;
        font-size: 15px;
    }
    circle {
        opacity: 0.5;
        stroke-dasharray: 1pt;
        stroke-width: 3;
    }
    svg {
        background-color: antiquewhite;
        padding: 5px;
    }
</style>
