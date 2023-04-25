<script>
  // @ts-nocheck
  import Moviecard from "$lib/moviecard.svelte";
  import ls from "localstorage-slim";
  import { onMount } from "svelte";
  import { djangoapi } from "../../app/stores";
  import { Jumper } from "svelte-loading-spinners";

  let currpage = 0;
  let totalmovie = Array();
  let currmovie = [];
  let isloading = true;

  const loadmovie = async () => {
    let headers = {};
    if (ls.get("jwt") != null)
      headers = { Authorization: `Bearer ${ls.get("jwt")}` };
    let res = await fetch(`${$djangoapi}/user/home/`, { headers });
    let data = await res.json();
    totalmovie = data;
    console.log(typeof totalmovie[0]);
    isloading = false;
  };
  $: currmovie = totalmovie.slice(currpage * 10, currpage * 10 + 10);

  onMount(loadmovie);
</script>

{#if isloading}
  <div class="w-fit m-auto mt-72">
    <Jumper color="#64748b" size="80" />
  </div>
{:else}
  <div class="flex flex-wrap px-10 justify-evenly">
    {#each currmovie as movie}
      <Moviecard
        poster={movie.Poster_path}
        imdb_id={movie.Imdb_id}
        name={movie.Title} />
    {/each}
  </div>

  <nav aria-label="Page navigation example" class="flex justify-center p-5">
    <ul class="inline-flex items-center -space-x-px">
      <li>
        <button
          on:click={() => {
            if (currpage == 1) currpage--;
          }}
          class="block px-3 py-2 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
          <span class="sr-only">Previous</span>
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
            ><path
              fill-rule="evenodd"
              d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
              clip-rule="evenodd" /></svg>
        </button>
      </li>
      <li>
        <button
          on:click={() => {
            currpage = 0;
          }}
          class="px-3 py-2 leading-tight border bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white btn"
          class:active={currpage === 0}>1</button>
      </li>
      <li>
        <button
          on:click={() => {
            currpage = 1;
          }}
          class="px-3 py-2 leading-tight border bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white btn"
          class:active={currpage === 1}>2</button>
      </li>
      <li>
        <button
          on:click={() => {
            if (currpage == 0) currpage++;
          }}
          class="block px-3 py-2 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
          <span class="sr-only">Next</span>
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
            ><path
              fill-rule="evenodd"
              d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
              clip-rule="evenodd" /></svg>
        </button>
      </li>
    </ul>
  </nav>
{/if}

<style>
  .active {
    background-color: #374151;
  }
</style>
