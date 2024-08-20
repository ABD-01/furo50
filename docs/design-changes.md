# Design Updates

This goes in depth of the stylesheet overrides made w.r.t. to the furo theme. These mostly serve as a developer note to remember the updates done.

## Scrolling Behaviour

Originally, brand text and search container had fixed pposition and could only scroll the rest of the navigation part.

Now the entire sidebar container can be scrolled.

## Layout Changes

```{raw} html
<style>
table {
    width:100%;
}
</style>
```

### Layout for max-width: 46em and max-width: 52em
* Only `content` is visible with width of 100%.

|                   Content                    |
|:--------------------------------------------:|
|                     100%                     |

### Layout for max-width: 67em
#### 52em < Total Width < 67em
* Only `content` is visible with width of 46em.

|                    Content                   |
|:--------------------------------------------:|
|                        46em                  |


### Layout for max-width: 82em
* `sidebar` and `content` are visible.
* `content` width: 46em.
* `sidebar` width: 18em.
* `sidebar` width: $\big( 100\% - (\text{full}_\text{width} - \text{sidebar}_\text{width} ) + \text{sidebar}_\text{width} \big)$

| Sidebar                                | Content |
|:--------------------------------------:|:-------:|
| `calc(18em + (100% - (82em - 18em)))`  | 46em    |



### Layout for min-width: 82em and above
* `sidebar`, `content`, and `toc-drawer` are visible.
* `sidebar` width: 18em.
* `sidebar` width: $\big( (100\% - \text{full}_\text{width}) + \text{sidebar}_\text{width} \big)$

* `toc-drawer` width: 12em.

| Sidebar                                | Content | TOC Drawer |
|:--------------------------------------:|:-------:|:----------:|
| `calc((100% - 82em) + 18em)`           | 46em    | 12em       |


### Layout for min-width: 100em
* `content` width: 52em
* `sidebar` max-width: 350px

| Sidebar | Content | TOC Drawer |
|:-------:|:-------:|:----------:|
| 350px   | 52em    | 12em       |


### Layout for min-width: 110em
* `content` width: 58em
* `sidebar` max-width: 350px

|     Sidebar     |     Content    |    TOC Drawer     |
|:---------------:|:--------------:|:-----------------:|
| 350px           | 58em           | 12em              |