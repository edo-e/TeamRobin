<script>
    import { scaleLog, scaleOrdinal, scaleLinear } from "d3-scale";
    import { schemeCategory10 } from "d3-scale-chromatic";
    import { selectAll, select } from "d3-selection";
    import { min, max } from "d3-array";
    import { each, transition_out } from "svelte/internal";
    //import  Dotting, { filename } from './App.svelte';

    export let datapoints = [];
    export let height_i = 0;

    const continentColor = scaleOrdinal(schemeCategory10);
    $: scale_mi = scaleLinear().domain([0, height_i]).range([height_i, 0]);
    //  width={(datapoints.length * 20).toString()}
    // height={(height_i).toString()}
</script>

<svg id="svg1" width={(datapoints.length * 20).toString()} height={(height_i).toString()}>
    {#each datapoints as datapoint}
        {#each datapoint.Female_1990 as female}
            <rect
                x={datapoint.X}
                y={scale_mi(female)}
                ry="3"
                rx="3"
                height="12"
                width="12"
            />
        {/each}

        {#each datapoint.Male_1990 as male}
            <rect
                x={datapoint.X}
                y={scale_mi(male)}
                ry="3"
                rx="3"
                height="12"
                width="12"
                class="male"
            />
        {/each}

        {#each datapoint.Female_1995 as female}
            <rect
                x={datapoint.X}
                y={scale_mi(female)}
                ry="3"
                rx="3"
                height="12"
                width="12"
            />
        {/each}
        {#each datapoint.Male_1995 as male}
            <rect
                x={datapoint.X}
                y={scale_mi(male)}
                ry="3"
                rx="3"
                height="12"
                width="12"
                class="male"
            />
        {/each}
        {#each datapoint.Female_2000 as female}
            <rect
                x={datapoint.X}
                y={scale_mi(female)}
                ry="3"
                rx="3"
                height="12"
                width="12"
            />
        {/each}
        {#each datapoint.Male_2000 as male}
            <rect
                x={datapoint.X}
                y={scale_mi(male)}
                ry="3"
                rx="3"
                height="12"
                width="12"
                class="male"
            />
        {/each}
        {#each datapoint.Female_2005 as female}
            <rect
                x={datapoint.X}
                y={scale_mi(female)}
                ry="3"
                rx="3"
                height="12"
                width="12"
            />
        {/each}
        {#each datapoint.Male_2005 as male}
            <rect
                x={datapoint.X}
                y={scale_mi(male)}
                ry="3"
                rx="3"
                height="12"
                width="12"
                class="male"
            />
        {/each}
        {#each datapoint.Female_2010 as female}
            <rect
                x={datapoint.X}
                y={scale_mi(female)}
                ry="3"
                rx="3"
                height="12"
                width="12"
            />
        {/each}
        {#each datapoint.Male_2010 as male}
            <rect
                x={datapoint.X}
                y={scale_mi(male)}
                ry="3"
                rx="3"
                height="12"
                width="12"
                class="male"
            />
        {/each}
        {#each datapoint.Female_2015 as female}
            <rect
                x={datapoint.X}
                y={scale_mi(female)}
                ry="3"
                rx="3"
                height="12"
                width="12"
            />
        {/each}
        {#each datapoint.Male_2015 as male}
            <rect
                x={datapoint.X}
                y={scale_mi(male)}
                ry="3"
                rx="3"
                height="12"
                width="12"
                class="male"
            />
        {/each}
        {#each datapoint.Female_2019 as female}
            <rect
                x={datapoint.X}
                y={scale_mi(female)}
                ry="3"
                rx="3"
                height="12"
                width="12"
            />
        {/each}
        {#each datapoint.Male_2019 as male}
            <rect
                x={datapoint.X}
                y={scale_mi(male)}
                ry="3"
                rx="3"
                height="12"
                width="12"
                class="male"
            />
        {/each}
        <line
        x1={datapoint.X}
        x2={datapoint.X+12}
        y1={scale_mi(datapoint.Y)}
        y2={scale_mi(datapoint.Y)}
        />
        <text
            x={datapoint.X}
            y={scale_mi(datapoint.Y)}
            text-anchor="start">1990</text
        >
        
    {/each}
</svg>
<svg id="svg1" width={(datapoints.length * 20).toString()} height={200}>
    {#each datapoints as datapoint}
        <text
            x={datapoint.X}
            y="0"
            transform="rotate(90,{datapoint.X},0)"
            text-anchor="start">{datapoint.Destination}</text
        >
    {/each}
</svg>

<style>
    text {
        opacity: 1;
        font: 15px Arial, sans-serif;
    }

    rect {
        opacity: 0.5;
        fill: red;
    }
    rect.male {
        opacity: 0.5;
        fill: blue;
    }
    line{
        opacity: 0.2;
        stroke: black;
        stroke-width: 2pt;
    }
    svg {
        background-color: antiquewhite;
        padding: 5px;
    }
</style>
