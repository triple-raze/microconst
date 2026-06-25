# Changelog

## 0.2.0
### Fixed
- Minor architecture rework
- Better naming (data -> entry)
### Added
- `key(literal: TypeForm[T]) -> Key[T]` - you can now pass Literal (pseudo-)supertype in function.
- Changelog

## 0.1.1
### Fixed
- Readme
- Architecture rework
### Added
- `Entry[T]` - internal, only for annotations. 

## 0.1.0
### Added
- `flag() -> str` 
- `key(converter: Callable[[str], T]) -> Key[T]`
- `Key[T]` - internal, only for annotations.