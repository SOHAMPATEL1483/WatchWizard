<script>
  // @ts-nocheck
  import ls from "localstorage-slim";
  import { djangoapi } from "../../app/stores";
  import { Jumper } from "svelte-loading-spinners";

  let isloading = false;
  let moviename = "";
  let search_results = [];
  const searchmovie = async () => {
    isloading = true;
    let headers = {};
    if (ls.get("jwt") != null)
      headers = { Authorization: `Bearer ${ls.get("jwt")}` };
    let res = await fetch(`${$djangoapi}/user/home/?name=${moviename}`, {
      headers,
    });
    let data = await res.json();
    // console.log(data);
    search_results = data;
    moviename = "";
    isloading = false;
  };
</script>

<form class="max-w-2xl mx-auto my-20 font-poppins px-5">
  <label
    for="default-search"
    class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
    >Search</label>
  <div class="relative">
    <div
      class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
      <svg
        aria-hidden="true"
        class="w-5 h-5 text-gray-500 dark:text-gray-400"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
        ><path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
    </div>
    <input
      type="search"
      bind:value={moviename}
      id="default-search"
      class="block w-full p-4 pl-10 text-sm border rounded-lg bg-gray-700 border-gray-600 dark:placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500"
      placeholder="Search Movies..."
      required />
    <button
      on:click={searchmovie}
      class="text-white absolute right-2.5 bottom-2.5 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-4 py-2 bg-primary-600 hover:bg-primary-700 focus:ring-primary-800"
      >Search</button>
  </div>
</form>

{#if isloading}
  <div class="w-fit h-fit m-auto">
    <Jumper color="#64748b" size="80" />
  </div>
{:else}
  {#each search_results as movie}
    <div class="px-5">
      <a
        href={"/movie/" + movie.Imdb_id}
        class="flex mx-auto my-5 font-poppins items-center bg-white border rounded-lg shadow max-w-2xl hover:bg-gray-100 border-gray-700 dark:bg-gray-700">
        <img
          class="object-cover rounded-l-lg h-32"
          src={"https://image.tmdb.org/t/p/w200" + movie.Poster_path}
          alt="" />
        <div class="flex flex-col justify-between p-4 ml-4">
          <h5 class="mb-2 text-xl font-bold tracking-wide text-slate-300">
            {movie.Title}
          </h5>
        </div>
      </a>
    </div>
  {:else}
    <p class="text-slate-300 font-poppins mx-auto w-fit">No Results</p>
  {/each}
{/if}
