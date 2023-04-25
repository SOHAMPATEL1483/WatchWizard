<script>
  // @ts-nocheck

  import "../app.css";
  import ls from "localstorage-slim";
  const signout = () => {
    ls.clear();
    location.reload();
  };
</script>

<nav class="bg-white border-gray-200 dark:bg-gray-800">
  <div
    class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
    <a href="/" class="flex items-center">
      <!-- <img src="/logo.png" class="h-8 mr-3" alt="" /> -->
      <span
        class="self-center text-xl md:text-2xl font-semibold font-Lexend whitespace-nowrap dark:text-white"
        >WatchWizard</span>
    </a>
    <div class="flex items-center md:order-2">
      {#if ls.get("jwt") === null}
        <a
          href="/login"
          type="button"
          class="text-white cursor-pointer focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 bg-primary-600 hover:bg-primary-700 focus:ring-primary-800"
          >Login</a>
      {:else}
        <a
          href="/user"
          type="button"
          class="flex mr-3 text-sm bg-gray-800 rounded-full
          md:mr-0 focus:ring-4 focus:ring-gray-600"
          id="user-menu-button"
          aria-expanded="false"
          data-dropdown-toggle="user-dropdown"
          data-dropdown-placement="bottom">
          <span class="sr-only">Open user menu</span>
          <!-- svelte-ignore a11y-img-redundant-alt -->
          <img
            class="w-8 h-8 rounded-full"
            src={`https://ui-avatars.com/api/?name=${ls.get(
              "username"
            )}&background=random`}
            alt="user photo" />
        </a>
        <button
          on:click={signout}
          type="button"
          class="text-white cursor-pointer focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-4 py-2 text-center mx-3 md:mr-0 bg-primary-600 hover:bg-primary-700 focus:ring-primary-800"
          >Sign Out</button>
      {/if}

      <button
        data-collapse-toggle="mobile-menu-2"
        type="button"
        class="inline-flex items-center p-2 ml-1 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
        aria-controls="mobile-menu-2"
        aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg
          class="w-6 h-6"
          aria-hidden="true"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
          ><path
            fill-rule="evenodd"
            d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
            clip-rule="evenodd" /></svg>
      </button>
    </div>
    <div
      class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1"
      id="mobile-menu-2">
      <ul
        class="flex flex-col font-Lexend p-4 md:p-0 mt-4 border rounded-lg md:flex-row md:space-x-8 md:mt-0 md:border-0 bg-gray-800 md:bg-gray-800 border-gray-700">
        <li>
          <a
            href="/home"
            class="block py-2 pl-3 pr-4 text-white md:hover:text-primary-400 rounded md:bg-transparent md:p-0"
            aria-current="page">Home</a>
        </li>
        <li>
          <a
            href="/search"
            class="block py-2 pl-3 pr-4 rounded md:hover:text-primary-400 md:p-0 text-white md:dark:hover:text-primary-400 hover:bg-gray-700 dark:hover:text-white md:hover:bg-transparent dark:border-gray-700"
            >Search</a>
        </li>
        <li>
          <a
            href="/"
            class="block py-2 pl-3 pr-4 rounded md:hover:text-primary-400 md:p-0 text-white md:dark:hover:text-primary-400 hover:bg-gray-700 dark:hover:text-white md:hover:bg-transparent dark:border-gray-700"
            >About</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<slot />
