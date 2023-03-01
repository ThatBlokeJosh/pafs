# PAFS: Python automatic folder sorter :snake:

## *An automatic :robot: downloads folder sorter writen in Python :snake: with JSON configuration*

---

# TODO:

- [ ]  Add Windows :desktop_computer: support

- [ ]   Add some form of system arguments :angry:

- [x]  Increase configuration :gear:

---

# How to configure

*The default path configuration should work for most Linux machines, however if you want to change the sorting path in any way then change the path in the conf.JSON file like so:*

```json
{
    "id": "Pictures",
    "path": "~/Personal/Pictures"
},
```

*in this example I changed the directory in which all picture format files go*

---

*To change the extension list, add the extension to the category that you want to sort that file format to, for example:*

```json
{
    "id": "Documents",
    "extensions": ["doc", "docx", "md"]
},
```

*in this example I added and removed some file extensions from the Documents category*
