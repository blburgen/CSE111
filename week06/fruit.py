def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(f"reverse: {fruit_list}")
  fruit_list.append("orange")
  print(f"append: {fruit_list}")
  fruit_list.insert(fruit_list.index("apple"),"cherry")
  print(f"insert: {fruit_list}")
  fruit_list.remove("banana")
  print(f"remove: {fruit_list}")
  print(f"pop {fruit_list.pop()}: {fruit_list}")
  fruit_list.sort()
  print(f"sorted: {fruit_list}")
  fruit_list.clear()
  print(f"clear: {fruit_list}")
  
if __name__ == "__main__":
    main()