## Website Downloader Python

このPythonライブラリは、ウェブサイトをローカルにダウンロードする機能を提供します。オフラインでのブラウジング、アーカイブ化、またはテストなど、さまざまな目的でウェブサイトのローカルコピーを作成するために使用できます。

### 機能

- ウェブページをダウンロードし、それに関連するCSS、JavaScript、画像などのリソースを含めます。
- ウェブページに埋め込まれた動画のダウンロードをサポートします。
- 相対URLと絶対URLを正しく処理します。
- ネットワークエラー、I/Oエラー、パースエラーなど、さまざまなシナリオのエラーハンドリングを提供します。

### 使用方法

このライブラリを使用したい場合は、リポジトリをローカルフォルダにクローンし、`pip install .`を実行してください。
以下は、Pythonから関数を呼び出す方法の例です：

```python
import website_downloader
website_downloader.save_website("https://example.com","パス")
```

### エラーハンドリング

このライブラリは、さまざまな失敗シナリオに対する包括的なエラーハンドリングを提供します。エラーはRequestError、IoError、UrlParseError、SelectorParseErrorなどのタイプに分類されます。これらのタイプに基づいてエラーを適切に処理できます。

### ライセンス

このプロジェクトはMITライセンスのもとで提供されています。詳細は[LICENSE](https://github.com/meowkawaiijp/WebSite-Copy/blob/main/README.md)ファイルを参照してください。

### 貢献

貢献は歓迎します！問題が発生した場合や改善の提案がある場合は、[GitHubリポジトリ](https://github.com/meowkawaiijp/rust_dll_website_copy)でIssueを開いてください。


